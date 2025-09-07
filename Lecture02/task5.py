talents=float(input("enter the talent:"))
pounds=float(input("enter te pound:"))
lots=float(input("enter the lots:"))

grams_total=(talents*20*32*13.3) + (pounds*32*13.3) + (lots*13.3)
kilogram=int(grams_total//1000)
grams=grams_total%1000
print("the weight in modern unit is",kilogram,"kilogram and", round(grams, 2),"grams")