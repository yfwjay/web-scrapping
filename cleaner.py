import pandas as pd

def cleaner_py():

    # Ill be making the books_data csv cleaner

    # read our csv

    df = pd.read_csv(r"/home/kabuga/projects/web_scrapping/projects/kenya_news_scraper/books_data.csv")

    # the price column has unwanted letters replace them appropriately

    df['price_clean'] = (df['price'].str.replace('Â' , '' , regex = False).str.replace('£' , '' , regex = False).str.strip().astype(float))

    # the column for rating they are in words map that to numbers

    rating_map = {
        'One' : 1 , 
        'Two' : 2 , 
        'Three' : 3 , 
        'Four' : 4 ,
        'Five' : 5
    }

    df['rating_number'] = df['rating'].map(rating_map)

    # also deal with duplicates we drop duplicate books

    # its size before

    before = len(df)
    df = df.drop_duplicates(subset = 'title')
    after = len(df)

    print(f"Removed {before - after} duplicate rows")


    # we now save a cleaner csv file

    df.to_csv('books_data_clean.csv' , index = False)

    print(f"Clean Rows = {len(df)}")
    print("Saved books_data_clean.csv")

    return df


# we perform some basic analysis


def basic_analysis(df):
    """Prints basic insights from the data."""
    print("\n--- Basic Analysis ---")
    print(f"Average price: £{df['price_clean'].mean():.2f}")
    print(f"Cheapest book: £{df['price_clean'].min():.2f}")
    print(f"Most expensive: £{df['price_clean'].max():.2f}")
    print(f"\nRating distribution:")
    print(df['rating'].value_counts())
    print(f"\nTop 5 highest rated books:")
    top = df[df['rating_number'] == 5][['title', 'price_clean']].head(5)
    print(top.to_string(index=False))

if __name__ == "__main__":
    df = cleaner_py()
    basic_analysis(df)