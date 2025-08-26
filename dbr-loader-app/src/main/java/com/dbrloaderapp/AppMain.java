package com.dbrloaderapp;

import org.apache.catalina.LifecycleException;
import org.apache.catalina.startup.Tomcat;
import org.springframework.web.context.support.XmlWebApplicationContext;
import org.springframework.web.servlet.DispatcherServlet;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class AppMain {
    public static void main(String[] args) throws LifecycleException {
        // Gets port config from application.properties
        Properties props = new Properties();
        try (InputStream input = AppMain.class.getClassLoader().getResourceAsStream("application.properties")) {
            props.load(input);
        } catch (IOException e) {}
        int port = Integer.parseInt(props.getProperty("server.port", "8080"));

        // Initialize the embedded Tomcat
        Tomcat tomcat = new Tomcat();
        tomcat.setPort(port);
        File base = new File(System.getProperty("java.io.tmpdir"));
        tomcat.getHost().setAppBase(base.getAbsolutePath());

        // Web context
        var ctx = tomcat.addContext("", base.getAbsolutePath());

        // Spring Context
        XmlWebApplicationContext springContext = new XmlWebApplicationContext();
        springContext.setConfigLocation("classpath:applicationContext.xml");

        // DispatcherServlet for REST API calls
        var dispatcher = new DispatcherServlet(springContext);
        Tomcat.addServlet(ctx, "dispatcher", dispatcher);
        ctx.addServletMappingDecoded("/api/*", "dispatcher");

        // Starts embedded Tomcat Server
        tomcat.start();
        System.out.println("App running in http://localhost:" + port + "/api");
        tomcat.getServer().await();
    }
}