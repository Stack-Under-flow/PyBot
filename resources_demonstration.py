from resources import Resources
#great naming scheme...

#I thought that this might help you to quickly evaluate the code
#admins may find it convenient to use the bot to modify resources

resources = Resources()

#initializing the class will give you access to .dictionary

print("Assembly resources:")
for url in resources.get_urls("Assembly"):
	print("\t" + url)

print("Trying to add duplicates doesn't work")
for url in resources.get_urls("Assembly"):
	print(resources.add_url("Assembly", url))

print("\n\nAssembly urls after adding")
for url in resources.get_urls("Assembly"):
	print("\t" + url)

print("\nGetting urls from a resource that doesnt exist")
print(resources.get_urls("hello!"))


print("\nAdding url for a resource with no URLS yet")
# add_urls now returns success or fail
print(resources.add_url("hello!", "http://google.com"))
print(resources.get_urls("hello!"))


# 'script' used to populate json from previous files
targets = ["Assembly", "C++", "C", "DiscordPy", "Git", "Hacking", "Java", "Linux", "Machine", "Mobile", "Python", "Shell", "Web"]
for t in targets:
	with open(f"Resources/{t}.txt", "r") as file:
		for line in file.readlines():
			resources.add_url(t.lower(), line)


# print(resources.get_urls("Assembly"))
# with open("Resources/Git.txt") as file:
# 	target = "Git"
# 	for line in file.readlines():
# 		resources.add_url(target, line)

# print(resources.get_urls("Git"))
resources.save_file()



