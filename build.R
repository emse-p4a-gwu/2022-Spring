# Render whole site
rmarkdown::render_site()

# Render README file
rmarkdown::render(input = 'README.Rmd', output_format = 'github_document')

# Render footer
source(file.path('child', 'footer.R'))
