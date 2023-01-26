import aspose.words as aw

# Load an existing Markdown document
doc = aw.Document("00-capa.md")

# Specify save options and set PDF compliance
saveOptions = aw.saving.PdfSaveOptions()
saveOptions.compliance = aw.saving.PdfCompliance.PDF17

# Save the document as PDF
doc.save(f".\\Output.pdf")