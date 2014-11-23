class Actuator < ActiveRecord::Base
	has_one :experiment
	has_many :actuations
	has_many :behaviors, through: :actuations

	mount_uploader :img, PictureUploader

end
