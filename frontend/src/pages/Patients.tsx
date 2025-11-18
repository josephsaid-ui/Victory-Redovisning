import { useState } from 'react'
import { Users, Plus, Search, Calendar } from 'lucide-react'

export default function Patients() {
  const [searchTerm, setSearchTerm] = useState('')

  const patients = [
    {
      id: 1,
      name: 'Anna Andersson',
      personnummer: '19800101-1234',
      lastVisit: '2024-11-10',
      diagnosis: 'Diabetesretinopati',
      nextAppointment: '2024-12-15'
    },
    {
      id: 2,
      name: 'Bengt Svensson',
      personnummer: '19750615-5678',
      lastVisit: '2024-11-08',
      diagnosis: 'Primär Öppenvinklat Glaukom',
      nextAppointment: '2024-11-25'
    },
    {
      id: 3,
      name: 'Cecilia Johansson',
      personnummer: '19920322-9012',
      lastVisit: '2024-11-12',
      diagnosis: 'Katarakt',
      nextAppointment: '2024-12-01'
    },
  ]

  const filteredPatients = patients.filter(patient =>
    patient.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    patient.personnummer.includes(searchTerm)
  )

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Patienter</h1>
          <p className="text-gray-600 mt-2">Hantera patientinformation (Demo)</p>
        </div>
        <button className="btn btn-primary flex items-center gap-2">
          <Plus className="w-5 h-5" />
          Ny patient
        </button>
      </div>

      {/* Search */}
      <div className="relative">
        <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
        <input
          type="text"
          placeholder="Sök patient (namn eller personnummer)..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="input pl-10"
        />
      </div>

      {/* Patient List */}
      <div className="grid grid-cols-1 gap-4">
        {filteredPatients.map((patient) => (
          <div key={patient.id} className="card hover:shadow-md transition-shadow cursor-pointer">
            <div className="flex items-start justify-between mb-4">
              <div className="flex items-start gap-3">
                <div className="p-3 bg-purple-100 rounded-full">
                  <Users className="w-6 h-6 text-purple-600" />
                </div>
                <div>
                  <h3 className="font-semibold text-lg">{patient.name}</h3>
                  <p className="text-sm text-gray-600">{patient.personnummer}</p>
                </div>
              </div>
              <span className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm font-medium">
                Aktiv
              </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-4 border-t border-gray-100">
              <div>
                <p className="text-xs text-gray-500 mb-1">Diagnos</p>
                <p className="font-medium text-sm">{patient.diagnosis}</p>
              </div>
              <div>
                <p className="text-xs text-gray-500 mb-1">Senaste besök</p>
                <p className="font-medium text-sm flex items-center gap-1">
                  <Calendar className="w-4 h-4 text-gray-400" />
                  {patient.lastVisit}
                </p>
              </div>
              <div>
                <p className="text-xs text-gray-500 mb-1">Nästa besök</p>
                <p className="font-medium text-sm flex items-center gap-1 text-primary-600">
                  <Calendar className="w-4 h-4" />
                  {patient.nextAppointment}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {filteredPatients.length === 0 && (
        <div className="card text-center py-12">
          <Users className="w-12 h-12 text-gray-400 mx-auto mb-3" />
          <p className="text-gray-600">Inga patienter hittades</p>
        </div>
      )}

      {/* Demo Notice */}
      <div className="card bg-yellow-50 border border-yellow-200">
        <p className="text-sm text-yellow-800">
          <strong>OBS:</strong> Detta är en demonstrationsfunktion. I en verklig miljö skulle detta integreras med
          patientjournalsystemet och följa GDPR och säkerhetsbestämmelser.
        </p>
      </div>
    </div>
  )
}
