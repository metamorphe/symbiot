require 'test_helper'

class ActuationsControllerTest < ActionController::TestCase
  setup do
    @actuation = actuations(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:actuations)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create actuation" do
    assert_difference('Actuation.count') do
      post :create, actuation: { actuator_id: @actuation.actuator_id, behavior_id: @actuation.behavior_id }
    end

    assert_redirected_to actuation_path(assigns(:actuation))
  end

  test "should show actuation" do
    get :show, id: @actuation
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @actuation
    assert_response :success
  end

  test "should update actuation" do
    patch :update, id: @actuation, actuation: { actuator_id: @actuation.actuator_id, behavior_id: @actuation.behavior_id }
    assert_redirected_to actuation_path(assigns(:actuation))
  end

  test "should destroy actuation" do
    assert_difference('Actuation.count', -1) do
      delete :destroy, id: @actuation
    end

    assert_redirected_to actuations_path
  end
end
