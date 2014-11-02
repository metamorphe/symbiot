FlixelLights::Application.routes.draw do
  resources :actuations

  resources :experiments

  resources :actuators

  root "light#index"

  get "light/view"
  get "light/wave"
  get "light/lb"
  get "light/index"
  get "light/library"
  get "light/synthesize"
  get "light/sequence"
  get "light/blinkm"
  post "light/create"

  get "behaviors/index"
  get "behaviors/new_stack"
  get "behaviors/new_wave"
  get "behaviors/record_wave"
  get "behaviors/get_states"
  post "behaviors/json_to_cpp"
  post "behaviors/create"
  resources :behaviors

  post "sequences/json_to_cpp"
  post "sequences/create"
  resources :sequences

  post "schemes/create"
  resources :schemes

  # The priority is based upon order of creation: first created -> highest priority.
  # See how all your routes lay out with "rake routes".

  # You can have the root of your site routed with "root"
  # root 'welcome#index'

  # Example of regular route:
  #   get 'products/:id' => 'catalog#view'

  # Example of named route that can be invoked with purchase_url(id: product.id)
  #   get 'products/:id/purchase' => 'catalog#purchase', as: :purchase

  # Example resource route (maps HTTP verbs to controller actions automatically):
  #   resources :products

  # Example resource route with options:
  #   resources :products do
  #     member do
  #       get 'short'
  #       post 'toggle'
  #     end
  #
  #     collection do
  #       get 'sold'
  #     end
  #   end

  # Example resource route with sub-resources:
  #   resources :products do
  #     resources :comments, :sales
  #     resource :seller
  #   end

  # Example resource route with more complex sub-resources:
  #   resources :products do
  #     resources :comments
  #     resources :sales do
  #       get 'recent', on: :collection
  #     end
  #   end

  # Example resource route with concerns:
  #   concern :toggleable do
  #     post 'toggle'
  #   end
  #   resources :posts, concerns: :toggleable
  #   resources :photos, concerns: :toggleable

  # Example resource route within a namespace:
  #   namespace :admin do
  #     # Directs /admin/products/* to Admin::ProductsController
  #     # (app/controllers/admin/products_controller.rb)
  #     resources :products
  #   end
end
