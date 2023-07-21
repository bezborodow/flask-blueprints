build:
	python3 -m build

publish:
	python3 -m twine upload --repository pypi dist/*

clean:
	rm dist/*
	rmdir dist/
