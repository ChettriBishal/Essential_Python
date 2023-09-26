// NOT violating SRP
// Only a code snippet doesn't actually work
class User {
    login(email: string, password: string) {}
  
    signup(email: string, password: string) {}
  
    assignRole(role: any) {}
  }
  
  // Violating SRP
  class ReportDocument {
    generateReport(data: any) {}
  
    createPDF(report: any) {}
  }