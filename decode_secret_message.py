#>py -m pip install requests
#>py -m pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

def render_character_grid(doc_url: str):
    #Extract document    
    response = requests.get(doc_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text,'html.parser')

    rows = soup.find_all('tr')
    data = []
    for row in rows[1:]: #skip the header row (i.e. x-coordinate | character | y-coordinate)
        cells = row.find_all('td')
        try:
            x = int(cells[0].text.strip())
            character = cells[1].text.strip()
            y = int(cells[2].text.strip())
            data.append({'x': x, 'char':character, 'y':y})
        except ValueError:
            continue #just in case, skip rows that are malformed

    if not data:
        print("No valid coordinates and characters found in document.")
        return

    # determine max coordinates for grid size
    max_x = max(entry['x'] for entry in data)
    max_y = max(entry['y'] for entry in data)

    # empty grid with max coordinates
    grid = [ [' ' for _ in range(max_x+1)] for _ in range(max_y + 1)]
    #print(grid)

    for entry in data:
        x = entry['x']
        y = entry['y']
        char = entry['char']
        grid[y][x] = char
    
    for row in grid[::-1]: #print from bottom to top, so it displays proper uppercase letters with the given document
        print(''.join(row))
    #print('\n'.join(''.join(row) for row in grid))

if __name__ == "__main__":
    #url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
    url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
    render_character_grid(url)