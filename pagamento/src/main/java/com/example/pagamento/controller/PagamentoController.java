package com.example.pagamento.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PagamentoController {

    @GetMapping("/pagamento")
    public String getInfo() {
        return "Simulação do serviço de pagamento.";
    }
}
