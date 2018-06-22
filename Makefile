RM=rm -rf
PYCACHE=__pycache__
PYC=*.pyc

# Just added to clean, nothing more

.PHONY:
	clean

clean:
	$(RM) $(PYCACHE) $(PYC)
