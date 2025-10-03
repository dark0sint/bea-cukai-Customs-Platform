    package main

    import (
        "github.com/gin-gonic/gin"
        "net/http"
    )

    func GetDeclarations(c *gin.Context) {
        decls, err := apiClient.GetDeclarations()
        if err != nil {
            c.HTML(http.StatusInternalServerError, "declarations.html", gin.H{"Error": err.Error()})
            return
        }
        c.HTML(http.StatusOK, "declarations.html", gin.H{"Declarations": decls})
    }
    
