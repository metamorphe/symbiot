class ComposerController < ApplicationController
	before_action :authenticate_user!
  def task
 	 # DESIGN PROMPT
  end

  def index
  	render :layout => "singe_page_app"
  end

  def diary
  end

  def library_selector
  	@library = Actuator.all
  	# .collect{|a| [a.name, {actuator: a, flavors: a.flavors}] }
  	# @library = Hash[@library]


  	# render :json => @library
  	render :layout => "singe_page_app"
  end
end
