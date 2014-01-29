TEX=pdflatex
PDF=slide.pdf

all: $(PDF)

SRC=$(wildcard *.tex)
IMG=$(wildcard image/*.png) 

slide.pdf: slide.tex $(IMG) $(SRC)
	$(TEX) $<
	$(TEX) $<
	rm *.aux *.log *.toc *.out *.nav *.snm

.PHONY: clean display

display:
	evince $(PDF) &

clean:
	rm *.aux *.log *.toc *.out *.nav *.snm *.pdf
