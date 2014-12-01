# encoding: UTF-8
# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20141130205843) do

  create_table "actuations", force: true do |t|
    t.integer  "flavor_id"
    t.integer  "behavior_id"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "actuators", force: true do |t|
    t.string   "name"
    t.datetime "created_at"
    t.datetime "updated_at"
    t.string   "picture"
  end

  create_table "behavior_links", force: true do |t|
    t.integer  "position"
    t.datetime "created_at"
    t.datetime "updated_at"
    t.string   "behavior_id"
    t.string   "sequence_id"
  end

  create_table "behaviors", force: true do |t|
    t.string   "name"
    t.float    "notification"
    t.float    "active"
    t.float    "unable"
    t.float    "low_energy"
    t.float    "turning_on"
    t.datetime "created_at"
    t.datetime "updated_at"
    t.text     "states"
    t.boolean  "is_smooth",    default: false
    t.boolean  "is_library",   default: false
  end

  create_table "experiments", force: true do |t|
    t.integer  "actuator_id"
    t.string   "physical_mag"
    t.string   "subjective_mag"
    t.string   "stimulus_cond"
    t.string   "continuum"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "flavors", force: true do |t|
    t.float    "alpha"
    t.datetime "created_at"
    t.datetime "updated_at"
    t.string   "img"
    t.integer  "actuator_id"
    t.string   "name"
  end

  create_table "schemes", force: true do |t|
    t.datetime "created_at"
    t.datetime "updated_at"
    t.string   "name"
  end

  create_table "sequence_links", force: true do |t|
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "sequences", force: true do |t|
    t.datetime "created_at"
    t.datetime "updated_at"
    t.string   "name"
  end

  create_table "tags", force: true do |t|
    t.integer  "behavior_id"
    t.string   "label"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  create_table "users", force: true do |t|
    t.string   "email",                  default: "", null: false
    t.string   "encrypted_password",     default: "", null: false
    t.string   "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.integer  "sign_in_count",          default: 0,  null: false
    t.datetime "current_sign_in_at"
    t.datetime "last_sign_in_at"
    t.string   "current_sign_in_ip"
    t.string   "last_sign_in_ip"
    t.datetime "created_at"
    t.datetime "updated_at"
  end

  add_index "users", ["email"], name: "index_users_on_email", unique: true, using: :btree
  add_index "users", ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true, using: :btree

end
