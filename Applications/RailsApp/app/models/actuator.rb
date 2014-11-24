class Actuator < ActiveRecord::Base
	has_one :experiment
	has_many :actuations
	has_many :behaviors, through: :actuations
	has_many :flavors
end
