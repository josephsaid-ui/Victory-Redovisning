import { useState } from 'react'
import { Search, Pill, Filter } from 'lucide-react'

export default function Medications() {
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedCategory, setSelectedCategory] = useState('all')

  const categories = ['all', 'Glaukom', 'Antibiotika', 'Anti-inflammatoriska', 'Smörjande', 'Anti-VEGF']

  const medications = [
    {
      name: 'Xalatan (Latanoprost)',
      category: 'Glaukom',
      type: 'Prostaglandinanalog',
      dosage: '1 droppe på kvällen',
      indication: 'Primär öppenvinklat glaukom'
    },
    {
      name: 'Ciloxan (Ciprofloxacin)',
      category: 'Antibiotika',
      type: 'Fluorokinolon',
      dosage: '1-2 droppar var 2-4h',
      indication: 'Bakteriell keratit, konjunktivit'
    },
    {
      name: 'Eylea (Aflibercept)',
      category: 'Anti-VEGF',
      type: 'Anti-VEGF',
      dosage: '2 mg intravitrealt',
      indication: 'Våt AMD, DME, venocklusioner'
    },
  ]

  const filteredMedications = medications.filter(med => {
    const matchesSearch = med.name.toLowerCase().includes(searchTerm.toLowerCase())
    const matchesCategory = selectedCategory === 'all' || med.category === selectedCategory
    return matchesSearch && matchesCategory
  })

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Läkemedelsdatabas</h1>
        <p className="text-gray-600 mt-2">100 ögonläkemedel med detaljerad information</p>
      </div>

      {/* Search and Filter */}
      <div className="flex flex-col md:flex-row gap-4">
        <div className="flex-1 relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
          <input
            type="text"
            placeholder="Sök läkemedel..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="input pl-10"
          />
        </div>
        <div className="flex items-center gap-2">
          <Filter className="w-5 h-5 text-gray-400" />
          <select
            value={selectedCategory}
            onChange={(e) => setSelectedCategory(e.target.value)}
            className="input"
          >
            {categories.map(cat => (
              <option key={cat} value={cat}>{cat === 'all' ? 'Alla kategorier' : cat}</option>
            ))}
          </select>
        </div>
      </div>

      {/* Medication List */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {filteredMedications.map((med, idx) => (
          <div key={idx} className="card hover:shadow-md transition-shadow cursor-pointer">
            <div className="flex items-start gap-3 mb-3">
              <div className="p-2 bg-green-100 rounded-lg">
                <Pill className="w-5 h-5 text-green-600" />
              </div>
              <div className="flex-1">
                <h3 className="font-semibold text-lg">{med.name}</h3>
                <p className="text-sm text-gray-600">{med.type}</p>
              </div>
              <span className="px-2 py-1 bg-blue-100 text-blue-800 rounded text-xs font-medium">
                {med.category}
              </span>
            </div>
            <div className="space-y-2 text-sm">
              <div className="flex items-start gap-2">
                <span className="font-medium text-gray-700 min-w-[80px]">Dosering:</span>
                <span className="text-gray-600">{med.dosage}</span>
              </div>
              <div className="flex items-start gap-2">
                <span className="font-medium text-gray-700 min-w-[80px]">Indikation:</span>
                <span className="text-gray-600">{med.indication}</span>
              </div>
            </div>
          </div>
        ))}
      </div>

      {filteredMedications.length === 0 && (
        <div className="card text-center py-12">
          <Pill className="w-12 h-12 text-gray-400 mx-auto mb-3" />
          <p className="text-gray-600">Inga läkemedel hittades</p>
        </div>
      )}
    </div>
  )
}
