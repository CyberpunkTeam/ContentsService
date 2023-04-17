Feature: CRUD Contents


  Scenario: Create content

    When escribo la publicacion "Agiles methologies"

    And la publico

    Then se me informa que se publico exitosamente


  Scenario: Create content with team
    Given que quiero crear un contenido para el equipo "Las papayas"

    When escribo la publicacion "Agiles methologies"

    And la publico

    Then se me informa que se publico exitosamente
