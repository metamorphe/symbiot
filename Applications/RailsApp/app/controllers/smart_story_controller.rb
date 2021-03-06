class SmartStoryController < ApplicationController
	def register
		file = File.read('devices.json')
		data_hash = JSON.parse(file)
		if data_hash.has_key?(params[:uuid])
			data_hash[params[:uuid]] = params[:modalities]
		else
			data_hash[params[:uuid]] = params[:modalities]
			render :json => params[:uuid].to_json
			File.open('devices.json', 'w') do |f|
				f.write(JSON.pretty_generate(data_hash))
			end
		end
	end
	def echo
		render :json => params
	end
	# generate based on nearby devices, segments with desired environment
	def new_story
		a = "New story. Push data to me by passing in UUIDs of nearby devices and segment descriptions"
		render :json => a.to_json
		if params.has_key?("uuid") and params.has_key?("nearby_devices") and params.has_key?("segments")
			env_hash = create_env(params)
			File.open('storyboard_environments/' + params[:uuid], 'w') do |f|
				f.write(JSON.pretty_generate(env_hash))
			end
		end
	end
 	# create a hash based on the available devices.
        # should generate a list of segments and which devices correspond to which.
        def create_env(params)
                env_hash = Hash.new
                file = File.read('devices.json')
                devices_hash = JSON.parse(file)
                nearby = params[:nearby_devices]
                #generate list of devices
                devices = Hash.new
                nearby.each {|index, uuid|
                #for uuid in nearby
                        devices[uuid] = devices_hash[uuid]
                #end
                }
                #for segment in params[:segments]
                params[:segments].each {|segment, attrs|
                        desired = params[segment]
                        least = Hash.new
                        improved = true
                        pool = Hash.new
                        level = 1
                        devices.each {|uuid, attrs| 
                                ls = least_squares(desired, attrs)
                                closest = ls
                                if ls == 0 
                                        return attrs 
                                else 
                                        pool[Hash[uuid: uuid]] = Hash[:least_squares: ls, :attrs: attrs]
                                end
                        }
                        while level < nearby.length and improved
                                improved = false
                                pool.each { |uuids, prev_info|
                                        this_improved = false
                                        if uuids.length == level
                                                nearby.each { |uuid, attrs|
                                                        new_attrs = sum_attrs(attrs, prev_info[:attrs])
                                                        new_ls = least_squares(new_attrs, desired)
                                                        if new_ls < prev_info[:least_squares]
                                                                pool[]
                                                                improved = true
                                                                this_improved = true
                                                                pool[uuids.merge(Hash[uuid:uuid])] = Hash[:least_squares: new_ls, :attrs: new_attrs]
                                                        end
                                                }
                                        end
                                        if this_improved
                                                pool.delete(uuids)
                                        end
                                }
                                level += 1
                        end
                        #for device in devices
                        #devices.each {|uuid, dev_attrs|
                                #least[uuid] = least_squares(desired, dev_attrs)
                        # env_hash[segment] =
                        #}
                        pool.each {|uuids, info|
                                if info[:least_squares] < closest
                                        closest = info[:least_squares]
                                        env_hash = uuids
                                end
                        }

                }
                return env_hash
        end

	def least_squares(desired, a, b)
		ls = 0
		for attr in desired
			ls += (a[attr] - b[attr])^2
		end
		return ls
	end
	def advance_story
		if params.has_key?("uuid") and params.has_key?("segment")
			file = File.read('storyboard_environments/' + params[:uuid])
			env_hash = JSON.parse(file)
			devices = env_hash[:segments][params[:segment]]
			for device in devices
				#actuate
			end
		end
	end
	def composer
		@story = Story.find(params[:story_id])
		@page = @story.story_pages.find{|s| s.page_number == params[:page_number].to_i}
		render :layout => "singe_page_app"
	end
end
