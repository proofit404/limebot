<?xml version="1.0"?>
<xsl:stylesheet
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns="http://www.w3.org/1999/xhtml" version="1.0">
  <xsl:template match="/page">
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <title>
	  <xsl:value-of select="/title/text()" />
	</title>
      </head>
      <body>
        <p>
	  <xsl:value-of select="/message/text()" />
	</p>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
