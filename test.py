from author import Author, Magazine, Article

# Sample Data
author1 = Author("Meso")
author2 = Author("Augustine")
mag1 = Magazine("Tech Times", "Technology")
mag2 = Magazine("Health Hub", "Health")

article1 = author1.add_article(mag1, "My life, my story")
article2 = author1.add_article(mag2, "God is good")
article3 = author2.add_article(mag1, "AI is the future")
article4 = author1.add_article(mag1, "Computer geek")

print(f"Author {author1.name} has written articles: {[a.title for a in author1.articles()]}")
print(f"Magazine {mag1.name} contributors: {[a.name for a in mag1.contributors()]}")
print(f"Top publisher: {Magazine.top_publisher().name}")