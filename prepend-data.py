f = open("book-data.csv");

line = f.readline();
print(line, end="");

line = f.readline();
text = ["Fantasy", "Science Fiction", "Mystery", "Biography", "Satire", "Horror", "Memoir", "Romance","Fable","Historical Fiction","Poetry"];

i = 0;
while line:

	if i == len(text):
		i = 0;

	print(text[i]+",", end="");
	print(line, end="");
	i += 1;
	line = f.readline();
