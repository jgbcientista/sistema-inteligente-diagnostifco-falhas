package com.example.estoque.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class EstoqueController {

    @GetMapping("/estoque")
    public String getInfo() {
        return "Simulação do serviço de estoque.";
    }
}
