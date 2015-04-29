class StoriesController < ApplicationController
  before_action :set_story, only: [:show, :edit, :update, :destroy]

  def ipad_output
    story = Story.find(params[:id])
    output = story.story_pages.map{|s|
      {
        type: s.storytype, 
        text_labels: s.story_texts.map{|st| {
            text: st.text, 
            fontSize: st.fontSize, 
            center: JSON.parse(st.center),
            textBackgroundHex: st.textBackgroundHex, 
            textBackgroundAlpha: st.textBackgroundAlpha,
            border: st.border 
          }
        },
        image_labels: s.story_images.map{|st| {
            imageURL: st.file_url, 
            imageSize: JSON.parse(st.size)
          }
        }
      }
    }[0]
      # story
      # story: story, 
      # pages: story.story_pages.map{|s| {text_labels: s.story_texts, image_labels: s.story_images}}

#     {
#     "type": "DrawingPrompterViewController",
#     "text_labels": [
#         {
#             "text": "Down in the meadow where animals flocked.\rWere four flanky mammals, on two legs they walked!\rCreatures that young Tom had not seen before.\rThe curious chipmunk just had to know more.",
#             "fontSize": 36,
#             "center": [
#                 0.5,
#                 0.8
#             ],
#             "textBackgroundHex": "FFFFFF",
#             "textBackgroundAlpha": 0.8,
#             "border": 20
#         }
#     ],
#     "image_labels": [
#         {
#             "imageURL": "https://api.built.io/v1/classes/story/objects/blt5fe6e3549984da5a/uploads/54949bdf2fa3e9e17b7c5768",
#             "imageSize": [
#                 1,
#                 1
#             ]
#         }
#     ]
# }

    render :json => output
  end
  # GET /stories
  # GET /stories.json
  def index
    @stories = Story.all
  end

  # GET /stories/1
  # GET /stories/1.json
  def show
  end

  # GET /stories/new
  def new
    @story = Story.new
  end

  # GET /stories/1/edit
  def edit
  end

  # POST /stories
  # POST /stories.json
  def create
    @story = Story.new(story_params)

    respond_to do |format|
      if @story.save
        format.html { redirect_to @story, notice: 'Story was successfully created.' }
        format.json { render action: 'show', status: :created, location: @story }
      else
        format.html { render action: 'new' }
        format.json { render json: @story.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /stories/1
  # PATCH/PUT /stories/1.json
  def update
    respond_to do |format|
      if @story.update(story_params)
        format.html { redirect_to @story, notice: 'Story was successfully updated.' }
        format.json { head :no_content }
      else
        format.html { render action: 'edit' }
        format.json { render json: @story.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /stories/1
  # DELETE /stories/1.json
  def destroy
    @story.destroy
    respond_to do |format|
      format.html { redirect_to stories_url }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_story
      @story = Story.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def story_params
      params.require(:story).permit(:title, :author)
    end
end
