# ruby sparse_format.rb lightbehaviors_harrison.json 

require 'json';
require 'fileutils'

@arduino_directory = "behaviors/cpp"
@command_directory = "behaviors/commands"
@matlab_directory = "behaviors/matlab"
@project_name = "expresso"



# takes in a values array of uint8 and output tuple array #[[value, duration]]
# duration is a scaling factor - use 1
def optimize_commands(name, values, duration)
	last_value = values[0];
	time_since_switch = 0;
	values = values.each_with_index.collect do |v,i|
		v = v.to_i
		uniqueness = last_value != v
		last_value = uniqueness ? v : last_value
		
		# if last element, output value and duration 
		if i == values.length - 1
			r = [last_value, (time_since_switch + 1) * duration]
			time_since_switch = 0
			r
		else
			# skip repeated values
			if !uniqueness 
				time_since_switch = time_since_switch + 1
				next
			else
				r = [last_value, (time_since_switch + 1) * duration]
				time_since_switch = 0
				r
			end
		end
	end
	# SPARSIFY
	values.compact!
	
	return values
end


def clean_values values
	# normalize to [0,1] float array
	min = values.min
	values.map!{ |v| (v - min)}
	max = values.max
	values.map!{ |v| max != 0 ? v / max : 1}

	# convert to uint8 array
	values.map!{ |v| ((1-v) * 255) }
	values
end

# Usage: process("all") => Generates header files for all behaviors
def process(flag, duration=1)
	if !ARGV[0]
		abort("Missing input file.")
	end

	filename = ARGV[0] # source file
	f = IO.read(filename)
	lb_hash = JSON.parse f


	create_directory(@arduino_directory)
	create_directory(@command_directory)
	create_directory(@matlab_directory)

	compression = []

	lb_hash.each do |name, values|
		name = parseName(name)
		values = clean_values(values)
		unoptimized = values.length
		values = optimize_commands(name, values, duration)
		optimized = values.length
		compression << {name: name, full: unoptimized, sparse: 1.0/(optimized/unoptimized.to_f ), bits: optimized * 16};

		array2arduino(@arduino_directory, name, values)
		array2command(@command_directory, name, values)
		array2matlab(@matlab_directory, name, values)
	end

	print_results(compression)
end

def hr size, marker
	line = []
	size.times do
		line << marker
	end
	line.join('');
end

def print_results(data)
	
	data= data.sort_by{|v| - v[:sparse] }
	header = data.first.keys().collect{|v| if v != :name then v.to_s.capitalize.center(5) else v.to_s.capitalize.center(30) end}
	header = header.join(' | ');
	hr_n = header.length
	p "COMPRESSION RESULTS".center(hr_n)
	p hr hr_n, "%"
	p header
	p hr hr_n, "-"
	rows = data.collect do |v|
		r = v.collect{|k, v| if k != :name then "#{"%5.0f" % v }" else v.to_s.ljust(30)  end }
		
	end
	rows.each do |r|
		p r.join(' | ');
	end
end

# name of behavior, float array, duration scalar (use 1)
def array2command(dirname, name, data, duration=1)
	File.open(dirname + "/" + name + "_lb.h", 'w') do |file| 
		sum = 0
		data_cum = data.collect do |v, d|
			sum += d 
			[v, sum]
		end
			
		# GENERATE ARDUINO CPP HEADER FILE
			# last = data.pop
			header(name, file);

			file.write "\tLogger *#{name.underscore};\n"
			file.write "\tvoid getLog(){\n"
			file.write "\t\t #{name.underscore} = new Logger(#{"%3.0f" % data_cum.length}, 0, 255);\n"

			data_cum.each do |v, d|
				file.write "\t\t#{name.underscore}->log(#{"%3.0f" % v}, #{"%3.0f" % d});\n"
			end
			file.write "\t}\n"
			footer(name, file);
		# END HEADER FILE
	end
end


def array2arduino(dirname, name, data, duration=1)
	File.open(dirname + "/" + name + "_lb.h", 'w') do |file| 

	

	# convert to hex code
	data_hex = data.map{ |v, d| ["0x%02x" % v, d]; }

	# GENERATE ARDUINO CPP HEADER FILE
		last = data_hex.pop
		header(name, file)
		file.write "blinkm_script_line #{name}[] = {\n"
		data_hex.each do |v, d|
			file.write "	{ #{d}, { 'n', #{hexify(v)}}},\n"
		end
		file.write "	{ #{last[1]}, { 'n', #{hexify(last[0])}}}\n"
		file.write "};\n"
		file.write "int script_#{name.downcase}_len = #{data.length};  // number of script lines above\n"
		footer(name, file);
	# END HEADER FILE
	end
end

def array2matlab(dirname, name, data, duration=1)
	File.open(dirname + "/" + name + "_lb.csv", 'w') do |file| 
		
		sum = 0
		data_cum = data.collect do |v, d|
			sum += d 
			[v, sum]
		end

		# GENERATE ARDUINO CPP HEADER FILE
			# last = data.pop
			# file.write data
			file.write data_cum.collect{|x| x[0]}.join(',') + "\n"
			file.write data_cum.collect{|x| x[1]}.join(',') + "\n"

		# END HEADER FILE
	end
end


def header (name, file)
	time = Time.new
	date =  time.strftime("%m/%d/%Y")
	
	file.write "//\n"
	file.write "//  #{name}_lb.h\n"
	file.write "//  #{@project_name} - #{name} Behavior\n"
	file.write "//\n"
	file.write "//  Created by Cesar Torres on #{date}.\n"
	file.write "//  Copyright (c) 2014 Cesar Torres. All rights reserved.\n"
	file.write "//\n"
	file.write "\n"
	file.write "#ifndef __#{name}__#{@project_name}__\n"
	file.write "#define __#{name}__#{@project_name}__\n"
	file.write "\n"

	libraries = ["Logger"]
	libraries.each do |l|
		file.write "#include \"#{l}.h\"\n"
	end
	file.write "\n"
end

def footer(name, file)
	file.write "\n"
	file.write "#endif /* defined(__#{name}__#{@project_name}__) */"
end


class String
  def underscore
    self.gsub(/::/, '/').
    gsub(/([A-Z]+)([A-Z][a-z])/,'\1_\2').
    gsub(/([a-z\d])([A-Z])/,'\1_\2').
    tr("-", "_").
    downcase
  end
end

def create_directory(dirname)
	unless File.directory?(dirname)
	  FileUtils.mkdir_p(dirname)
	end
end

def unparseName b
 "/lb/LB_#{b}.svg" 
end
def parseName b
 b.split('/lb/LB_')[1].split('.')[0] 
end
def hexify(v) 
	[v,v,v].join(',') 
end

process("all");