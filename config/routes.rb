Rails.application.routes.draw do
  get 'news/index' => "news#index" , as: :news_index
  post 'news/vote/:id' => "news#vote" , as: :news_vote 
  post 'news/devote/:id' => "news#devote" , as: :news_devote 

  root "news#index"

end
