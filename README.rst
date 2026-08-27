===============
politikus.theme
===============

Diazo theme for the Politikus site, targeting the Plone 6.2 Classic UI.

The theme is based on the Plone 6.2 ``plonetheme.barceloneta`` layout
(Bootstrap 5 markup).  ``theme/css/theme.css`` ships the barceloneta
stylesheet with the Politikus custom styles appended at the bottom; the
Roboto fonts (``theme/roboto/``) and the theme icons are vendored in the
theme directory, mirroring the barceloneta layout:

- ``.newsImageContainer`` — full-width news/issue images with caption styling
- ``.image-grid-2x2`` — two-column image grid (TinyMCE template, see
  ``theme/tinymce-templates/image-grid-2x2.html``)

Installation
------------

Install politikus.theme by adding it to your buildout::

    [buildout]

    ...

    eggs =
        politikus.theme

and then running ``bin/buildout``.  Create or open a Plone site and enable
the add-on from the Plone Add-ons screen; the profile installs and enables
the theme.

Uninstalling re-enables the stock barceloneta theme.

License
-------

The project is licensed under the GPLv2.
