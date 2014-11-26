json.array!(@flavors) do |flavor|
  json.extract! flavor, :id, :alpha
  json.url flavor_url(flavor, format: :json)
end
