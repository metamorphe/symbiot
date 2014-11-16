class Behavior < ActiveRecord::Base

	has_many :behavior_links, dependent: :destroy
	has_many :sequences, through: :behavior_links

	has_many :actuations
	has_many :actuators, through: :actuations

	has_many :experiments

	def states
		if self[:states]
			self[:states].split(',').map{|x| x.to_f}
		else
			# foo
		end
	end

	def states=(_states)
		self[:states] = _states.join(',')
	end

	validates :name, presence: true
	validates_uniqueness_of :name
	validates :states, presence: true

	# number of top-category behaviors shown by filters
	SCORE_THRESHOLD = 5

	META_ATTRIBUTES = ["id", "created_at", "updated_at"]
	MAIN_ATTRS = self.attribute_names - META_ATTRIBUTES
	ARRAY_ATTRS = ["states"]
	STRING_ATTRS = ["name"]
	NUMBER_ATTRS = MAIN_ATTRS - ARRAY_ATTRS - STRING_ATTRS

	def self.get_main_attrs
		MAIN_ATTRS
	end

	def self.get_array_attrs
		ARRAY_ATTRS
	end

	def self.get_string_attrs
		STRING_ATTRS
	end

	def self.get_number_attrs
		NUMBER_ATTRS
	end

	def self.get_top_notification
		self._get_top_category "notification"
	end

	def self.get_top_active
		self._get_top_category "active"
	end

	def self.get_top_unable
		self._get_top_category "unable"
	end

	def self.get_top_low_energy
		self._get_top_category "low_energy"
	end

	def self.get_top_turning_on
		self._get_top_category "turning_on"
	end

	def self._get_top_category(category)
		self.order("#{category} DESC").limit(SCORE_THRESHOLD)
			.map{ |behavior| behavior.name }.to_json.html_safe
	end

	def self.get_smooths
		self.where("is_smooth", true).order("is_smooth DESC")
			.map{ |behavior| behavior.name }.to_json.html_safe
	end

	def self.json_to_cpp(json_data)
		name = json_data["behavior"]["name"]
		values = json_data["behavior"]["states"]
		values = values.map(&:to_f)
		self.array2cpp(name, values);
	end

	def self.compress(name, values, duration=1)
		self.array2cpp(name, values, duration=1)
	end

	# TODO: make metamethod to get to_actuator methods to turn pure
	# Behaviors into actuator-adjusted Behavior subclasses
	# !ACTUATORS.each do |actuator|
	# 	define_method("to_#{actuator}") do
	# 		#code body goes here
	# 	end
	# end

	private

		def self.array2cpp(name, values, duration=1)
			self.generate_arduino_code(name, values, duration)
		end

		def self.generate_arduino_code(name, values, duration=1)
			File.open(name + "_lb.h", 'w') do |file| 
				values = clean_values(values)
				values = optimize_commands(values, duration)

				# convert to hex code
				values.map!{ |v, d| ["0x%02x" % v, d]; }
				
				# GENERATE ARDUINO CPP HEADER FILE
					last = values.pop
					header(name, file)
					file.write "blinkm_script_line #{name}[] = {\n"
					values.each do |v, d|
						file.write "{ #{d}, { 'n', #{hexify(v)}}},\n"
					end
					file.write "	{ #{last[1]}, { 'n', #{hexify(last[0])}}}\n"
					file.write "};\n"
					file.write "int script_#{name.downcase}_len = #{values.length};  // number of script lines above\n"
					footer(name, file);
				# END HEADER FILE
			end
			return IO.read(name + "_lb.h")
		end

		def self.unparseName b
			"/lb/LB_#{b}.svg"
		end

		def self.parseName b
			b.split('/lb/LB_')[1].split('.')[0]
		end

		def self.hexify(v)
			[v,v,v].join(',')
		end

		# takes in a values array of uint8 and output tuple array #[[time, value]]
		# duration is a scaling factor - use 1
		def self.optimize_commands(values, duration)
			cmd = 'python bin/manifold/manifold.py compact "#{values.to_s}"'
			result = `#{cmd}`
			arr = JSON.parse(result)
			return arr
		end

		def self.clean_values values
			# normalize to [0,1] float array
			min = values.min
			values.map!{ |v| (v - min)}
			max = values.max
			values.map!{ |v| max != 0 ? v / max : 1}

			# convert to uint8 array
			values.map!{ |v| (v * 255) }
			values
		end

		def self.header (name, file)
			file.write "//\n"
			file.write "//  #{name}_lb.h\n"
			file.write "//  Flixels - #{name} Light Behavior\n"
			file.write "//\n"
			file.write "//  Created by Cesar Torres on 7/2/14.\n"
			file.write "//  Copyright (c) 2014 Cesar Torres. All rights reserved.\n"
			file.write "//\n"
			file.write "\n"
			file.write "#ifndef __#{name}__flixel__\n"
			file.write "#define __#{name}__flixel__\n"
			file.write "\n"
			file.write "#include \"BlinkM_funcs.h\"\n"
		end

		def self.footer(name, file)
			file.write "#endif /* defined(__#{name}__flixel__) */"
		end

end
