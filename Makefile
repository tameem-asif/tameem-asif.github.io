.PHONY: clean
clean:
	find docs/ ! -name styles ! -name "*.css" ! -name images ! -name "*.png" ! -name "*.jpg" ! -name "*.svg" ! -name resume ! -name "*.pdf" ! -name CNAME -delete