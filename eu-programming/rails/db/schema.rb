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

ActiveRecord::Schema.define(version: 20140627093003) do

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

end
