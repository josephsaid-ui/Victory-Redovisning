import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import Diseases from './pages/Diseases'
import Medications from './pages/Medications'
import SymptomChecker from './pages/SymptomChecker'
import Patients from './pages/Patients'

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/diseases" element={<Diseases />} />
        <Route path="/medications" element={<Medications />} />
        <Route path="/symptom-checker" element={<SymptomChecker />} />
        <Route path="/patients" element={<Patients />} />
      </Routes>
    </Layout>
  )
}

export default App
