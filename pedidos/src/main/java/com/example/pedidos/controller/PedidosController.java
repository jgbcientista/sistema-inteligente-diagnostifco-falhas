package com.example.pedidos.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PedidosController {

    @GetMapping("/pedidos")
    public String getInfo() {
        return "Simulação do serviço de pedidos.";
    }
}
