require 'test_helper'

class ExperimentsControllerTest < ActionController::TestCase
  setup do
    @experiment = experiments(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:experiments)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create experiment" do
    assert_difference('Experiment.count') do
      post :create, experiment: { actuator_id: @experiment.actuator_id, continuum: @experiment.continuum, physical_mag: @experiment.physical_mag, stimulus_cond: @experiment.stimulus_cond, subjective_mag: @experiment.subjective_mag }
    end

    assert_redirected_to experiment_path(assigns(:experiment))
  end

  test "should show experiment" do
    get :show, id: @experiment
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @experiment
    assert_response :success
  end

  test "should update experiment" do
    patch :update, id: @experiment, experiment: { actuator_id: @experiment.actuator_id, continuum: @experiment.continuum, physical_mag: @experiment.physical_mag, stimulus_cond: @experiment.stimulus_cond, subjective_mag: @experiment.subjective_mag }
    assert_redirected_to experiment_path(assigns(:experiment))
  end

  test "should destroy experiment" do
    assert_difference('Experiment.count', -1) do
      delete :destroy, id: @experiment
    end

    assert_redirected_to experiments_path
  end
end
