package com.dbrloaderapp.controller;

import com.dbrloaderapp.model.Client;
import com.dbrloaderapp.service.ClientService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/client")
public class ClientController {
    private final ClientService clientService;

    @Autowired
    public ClientController(ClientService service) {
        this.clientService = service;
    }

    @GetMapping
    public List<Client> getAllClients() {
        return clientService.findAll();
    }
}
