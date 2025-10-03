    package main

    import (
        "bytes"
        "encoding/json"
        "fmt"
        "io"
        "net/http"
    )

    type Declaration struct {
        ID        int     `json:"id"`
        CargoType string  `json:"cargo_type"`
        Value     float64 `json:"value"`
    }

    var apiClient = &http.Client{}

    func GetDeclarations() ([]Declaration, error) {
        resp, err := apiClient.Get("http://localhost:5000/api/declarations")
        if err != nil {
            return nil, err
        }
        defer resp.Body.Close()

        body, err := io.ReadAll(resp.Body)
        if err != nil {
            return nil, err
        }

        var decls []Declaration
        json.Unmarshal(body, &decls)
        return decls, nil
    }

    // Add more functions like PostDeclaration, Login as needed
    
