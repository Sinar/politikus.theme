Changelog
=========


2.0a1 (unreleased)
------------------

- Rebase the Diazo theme on the Plone 6.2 Classic UI: ``theme/index.html``
  and ``theme/rules.xml`` now match the ``plonetheme.barceloneta`` 4.0
  layout (Bootstrap 5 markup, ``#portal-globalnav``, ``.card`` portlets),
  so the theme themes Plone 6.2 pages correctly.
- Replace the Plone 5 era less build with a single ``theme/css/theme.css``:
  the Plone 6.2 barceloneta stylesheet plus the Politikus custom styles
  (``.newsImageContainer``, ``.image-grid-2x2``).  Roboto fonts and the
  apple-touch icons are vendored in the theme directory (relative paths,
  same layout as ``plonetheme.barceloneta``).
- Drop the CDN Bootstrap 4 / jQuery / popper includes from the theme head;
  Plone 6.2 barceloneta provides its own Bootstrap 5 assets.
- Remove legacy parts: the vendored Plone 5 ``barceloneta/`` theme copy
  (less, fonts, icons), the ``less/`` sources and 6152-line compiled CSS,
  the grunt/npm build (``Gruntfile.js``, ``package.json``), the
  ``test_plone43/50/51/52.cfg`` and ``constraints_ploneXX.txt`` files,
  ``tox.ini``, ``.travis.yml``, ``.gitlab-ci.yml`` and the generator
  buildout scaffolding (``base.cfg``, ``bobtemplate.cfg``, ``buildout.cfg``,
  ``requirements.txt``, ``DEVELOP*.rst``, ``docs/``).
- Drop the unused ``plone.app.dexterity`` requirement.
  [kaerumy]


1.0a1
------------------

- Initial release.
  [kaerumy]
