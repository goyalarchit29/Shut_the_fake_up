class Article < ActiveRecord::Base
	has_attached_file :avatar,  default_url: "/images/:style/missing.png"
  validates_attachment_content_type :avatar, content_type: /\Aimage\/.*\z/
end
