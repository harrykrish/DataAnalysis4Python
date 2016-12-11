import argparse
parser = argparse.ArgumentParser()
parser.add_argument("city", help="City Name",
                    type=str)
parser.add_argument("category", help="category - Hotels, Restaurants or attractions",
                    type=str)


args = parser.parse_args()
searchh=args.category.lower()
v=['hotels','restaurants','attractions']
if(searchh not in v):
    parser.error('Category must be hotels,restaurants or attractions')

cityy=args.city
categoryy=args.category
print(cityy)
print(categoryy)






