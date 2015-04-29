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
	# generate based on nearby devices, segments with desired environment
	def new_story
		a = "New story"
		render :json => a.to_json
	end
end
