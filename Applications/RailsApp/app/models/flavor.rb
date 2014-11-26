class Flavor < ActiveRecord::Base
	belongs_to :actuator
	mount_uploader :img, PictureUploader
end
