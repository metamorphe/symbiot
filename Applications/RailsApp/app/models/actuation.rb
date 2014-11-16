class Actuation < ActiveRecord::Base
	belongs_to :actuator
	belongs_to :behavior
end