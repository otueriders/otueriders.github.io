import csv

def generate_card_html(image_ref, caption, contributor, date):
    # Generate a unique identifier for each image
    image_id = f"image_{image_ref.replace('.', '_')}"

    # Define the HTML template with CSS styling for images and onclick event
    html_template = f'''
        <div class="col">
          <div class="card shadow-sm">
            <img
              src="../images/gallery/{image_ref}"
              alt="{image_ref} failed to load.."
              class="card-img-top"
              style="width: 100%; height: 200px; object-fit: cover; cursor: pointer;"
              onclick="openImageViewer('../images/gallery/{image_ref}');"
            >  <!-- Adjust the height as needed -->
            <div class="card-body">
              <p class="card-text">{caption}</p>
              <div class="d-flex justify-content-between align-items-center">
                <small class="fw-bold">{contributor}</small>
                <small class="text-muted">{date}</small>
              </div>
            </div>
          </div>
        </div>
    '''

    return html_template


def start_gallery_CMS():
    # Define the CSV file name
    csv_file = 'gallery.csv'

    # Create an empty string to store the generated HTML
    html_content = ''

    try:
        with open(csv_file, 'r', newline='') as file:
            # Create a CSV reader
            csv_reader = csv.DictReader(file)

            # Initialize a counter to keep track of records printed
            record_count = 0

            # Iterate over each row in the CSV file
            for row in csv_reader:
                image_ref = row['image_ref']
                caption = row['caption']
                contributor = row['contributor']
                date = row['date']

                # Generate the HTML for the current row and add it to the content
                html_content += generate_card_html(image_ref, caption, contributor, date)

    except FileNotFoundError:
        print(f"The file '{csv_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Read the template file 'modules/templates/gallery_template.html'
    template_file_path = 'modules/templates/gallery_template.html'
    with open(template_file_path, 'r') as template_file:
        template_content = template_file.read()

    # Replace '{CONTENT INJECTED HERE}' with the generated HTML content
    final_html = template_content.replace('{CONTENT INJECTED HERE}', html_content)

    # Write the final HTML to a new file '../gallery/index.html'
    with open('../gallery/index.html', 'w') as output_file:
        output_file.write(final_html)

    print(f"[GALLERY] HTML content has been saved to '../gallery/index.html'")
