class NewsController < ApplicationController
  def index
  	@data = Article.all ;
  	
  end

  def vote
  	@id = params[:id] ;
  	@x = Article.find(params[:id]) ;
  	@x.votes+=1 ;
  	@x.save

  
  end

  def devote
  	@id = params[:id] ;
  	@x = Article.find(params[:id]) ;
  	@x.votes-=1 ;
  	@x.save
  end
end
