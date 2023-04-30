Feature: CRUD Contents


  Scenario: Create content

    When escribo la publicacion "Agiles methologies"

    And portada con la imagen "cover.png"

    And la publico

    Then se me informa que se publico exitosamente


  Scenario: Create content with team
    Given que quiero crear un contenido para el equipo "Las papayas"

    When escribo la publicacion "Agiles methologies"

    And la publico

    Then se me informa que se publico exitosamente


  Scenario: Update content
    Given que existe un contenido con titulo "Agile methodologies", portada "cover.png"

    When edito el titulo a "New Agile"

    Then veo que se cambio el titulo a "New Agile"

  Scenario: Delete content
    Given que existe un contenido con titulo "Agile methodologies", portada "cover.png"

    When elimino el contenido

    Then se me informa que se elimino correctamente
