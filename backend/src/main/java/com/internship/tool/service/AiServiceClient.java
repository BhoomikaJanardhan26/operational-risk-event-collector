package com.internship.tool.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@Service
public class AiServiceClient {

    @Value("${ai.service.url:http://localhost:5000}")
    private String aiServiceUrl;

    private final RestTemplate restTemplate;

    public AiServiceClient() {
        this.restTemplate = new RestTemplate();
        // Set 10s timeout if customizing RestTemplate request factory
    }

    public String describeRisk(String text) {
        return callAiService("/describe", text);
    }

    public String recommendActions(String text) {
        return callAiService("/recommend", text);
    }

    public String generateReport(String text) {
        return callAiService("/generate-report", text);
    }

    private String callAiService(String endpoint, String text) {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);

            Map<String, String> requestBody = new HashMap<>();
            requestBody.put("text", text);

            HttpEntity<Map<String, String>> request = new HttpEntity<>(requestBody, headers);

            ResponseEntity<String> response = restTemplate.postForEntity(
                    aiServiceUrl + endpoint, request, String.class);

            return response.getBody();
        } catch (Exception e) {
            System.err.println("Error calling AI Service: " + e.getMessage());
            return null; // Return null on error
        }
    }
}
