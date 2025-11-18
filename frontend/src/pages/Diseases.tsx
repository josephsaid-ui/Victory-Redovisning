import { useState } from 'react'
import { Search, AlertCircle, Filter } from 'lucide-react'

export default function Diseases() {
  const [searchTerm, setSearchTerm] = useState('')
  const [selectedCategory, setSelectedCategory] = useState('all')

  const categories = ['all', 'Retina', 'Glaukom', 'Katarakt', 'Hornhinna', 'Inflammatoriska']

  const diseases = [
    {
      name: 'Retinal Avlossning - Rhegmatogen',
      category: 'Retina',
      urgency: 'emergency',
      symptoms: ['Ljusblixtar', 'Floaters', 'Synfältsbortfall']
    },
    {
      name: 'Bakteriell Keratit',
      category: 'Hornhinna',
      urgency: 'emergency',
      symptoms: ['Ögonsmärta', 'Synnedsättning', 'Korneal infiltrat']
    },
    {
      name: 'Primär Öppenvinklat Glaukom (POAG)',
      category: 'Glaukom',
      urgency: 'routine',
      symptoms: ['Synfältsdefekter', 'Förhöjt IOP', 'Optikusskada']
    },
  ]

  const filteredDiseases = diseases.filter(disease => {
    const matchesSearch = disease.name.toLowerCase().includes(searchTerm.toLowerCase())
    const matchesCategory = selectedCategory === 'all' || disease.category === selectedCategory
    return matchesSearch && matchesCategory
  })

  const getUrgencyColor = (urgency: string) => {
    switch(urgency) {
      case 'emergency': return 'bg-red-100 text-red-800'
      case 'urgent': return 'bg-yellow-100 text-yellow-800'
      default: return 'bg-green-100 text-green-800'
    }
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Sjukdomsdatabas</h1>
        <p className="text-gray-600 mt-2">200 ögonsjukdomar med detaljerad information</p>
      </div>

      {/* Search and Filter */}
      <div className="flex flex-col md:flex-row gap-4">
        <div className="flex-1 relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
          <input
            type="text"
            placeholder="Sök sjukdom..."
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

      {/* Disease List */}
      <div className="grid grid-cols-1 gap-4">
        {filteredDiseases.map((disease, idx) => (
          <div key={idx} className="card hover:shadow-md transition-shadow cursor-pointer">
            <div className="flex items-start justify-between mb-3">
              <div>
                <h3 className="font-semibold text-lg">{disease.name}</h3>
                <p className="text-sm text-gray-600">{disease.category}</p>
              </div>
              <span className={'px-3 py-1 rounded-full text-xs font-medium ' + getUrgencyColor(disease.urgency)}>
                {disease.urgency}
              </span>
            </div>
            <div className="flex flex-wrap gap-2">
              {disease.symptoms.map((symptom, sidx) => (
                <span key={sidx} className="px-2 py-1 bg-gray-100 rounded text-sm">
                  {symptom}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>

      {filteredDiseases.length === 0 && (
        <div className="card text-center py-12">
          <AlertCircle className="w-12 h-12 text-gray-400 mx-auto mb-3" />
          <p className="text-gray-600">Inga sjukdomar hittades</p>
        </div>
      )}
    </div>
  )
}
