import { useState } from 'react'
import { Search, Send, AlertCircle } from 'lucide-react'

export default function SymptomChecker() {
  const [symptoms, setSymptoms] = useState('')
  const [results, setResults] = useState<any[]>([])
  const [loading, setLoading] = useState(false)

  const handleAnalyze = async () => {
    if (!symptoms.trim()) return

    setLoading(true)
    // Simulate API call
    setTimeout(() => {
      setResults([
        {
          disease: 'Bakteriell Keratit',
          probability: 'Hög',
          urgency: 'Emergency',
          matchingSymptoms: ['Ögonsmärta', 'Synnedsättning', 'Röda ögon'],
          recommendations: 'AKUT: Kontakta ögonläkare omedelbart. Fluorokinolon-droppar var 2h.'
        },
        {
          disease: 'Konjunktivit',
          probability: 'Medel',
          urgency: 'Urgent',
          matchingSymptoms: ['Röda ögon', 'Sekret'],
          recommendations: 'Antibiotika-droppar. Kontakta vårdcentral eller ögonläkare.'
        },
      ])
      setLoading(false)
    }, 1500)
  }

  const getUrgencyColor = (urgency: string) => {
    switch(urgency) {
      case 'Emergency': return 'bg-red-100 text-red-800 border-red-200'
      case 'Urgent': return 'bg-yellow-100 text-yellow-800 border-yellow-200'
      default: return 'bg-green-100 text-green-800 border-green-200'
    }
  }

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-gray-900">Symtomchecker</h1>
        <p className="text-gray-600 mt-2">AI-driven symptomanalys och differentialdiagnostik</p>
      </div>

      {/* Input */}
      <div className="card">
        <label className="block font-medium text-gray-700 mb-2">
          Beskriv symtomen
        </label>
        <textarea
          value={symptoms}
          onChange={(e) => setSymptoms(e.target.value)}
          placeholder="T.ex. 'Patient klagar på ögonsmärta, rodnad, och synnedsättning i vänster öga sedan igår...'"
          className="input min-h-[150px] resize-none"
        />
        <button
          onClick={handleAnalyze}
          disabled={loading || !symptoms.trim()}
          className="btn btn-primary mt-4 flex items-center gap-2"
        >
          {loading ? (
            <>Analyserar...</>
          ) : (
            <>
              <Send className="w-4 h-4" />
              Analysera symtom
            </>
          )}
        </button>
      </div>

      {/* Results */}
      {results.length > 0 && (
        <div className="space-y-4">
          <h2 className="text-xl font-semibold">Möjliga diagnoser</h2>
          {results.map((result, idx) => (
            <div key={idx} className={'card border-l-4 ' + getUrgencyColor(result.urgency)}>
              <div className="flex items-start justify-between mb-3">
                <div>
                  <h3 className="font-semibold text-lg">{result.disease}</h3>
                  <p className="text-sm text-gray-600">Sannolikhet: {result.probability}</p>
                </div>
                <span className={'px-3 py-1 rounded-full text-xs font-medium border ' + getUrgencyColor(result.urgency)}>
                  {result.urgency}
                </span>
              </div>

              <div className="space-y-3">
                <div>
                  <h4 className="font-medium text-sm text-gray-700 mb-2">Matchande symtom:</h4>
                  <div className="flex flex-wrap gap-2">
                    {result.matchingSymptoms.map((symptom: string, sidx: number) => (
                      <span key={sidx} className="px-2 py-1 bg-blue-50 text-blue-700 rounded text-sm">
                        {symptom}
                      </span>
                    ))}
                  </div>
                </div>

                <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3">
                  <div className="flex items-start gap-2">
                    <AlertCircle className="w-5 h-5 text-yellow-700 flex-shrink-0 mt-0.5" />
                    <div>
                      <h4 className="font-medium text-sm text-yellow-900 mb-1">Rekommendationer:</h4>
                      <p className="text-sm text-yellow-800">{result.recommendations}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Disclaimer */}
      <div className="card bg-blue-50 border border-blue-200">
        <div className="flex items-start gap-3">
          <AlertCircle className="w-5 h-5 text-blue-700 flex-shrink-0 mt-0.5" />
          <div>
            <h3 className="font-medium text-blue-900 mb-1">Viktig information</h3>
            <p className="text-sm text-blue-800">
              Detta är ett AI-baserat verktyg för utbildning och stöd. Det ersätter INTE klinisk bedömning.
              Vid akuta symtom, kontakta alltid läkare omedelbart.
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
