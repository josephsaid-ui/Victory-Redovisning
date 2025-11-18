import { Eye, Database, Pill, Users, AlertCircle } from 'lucide-react'

export default function Dashboard() {
  const stats = [
    { name: 'Totala sjukdomar', value: '200', icon: Database, color: 'bg-blue-500' },
    { name: 'Läkemedel', value: '100', icon: Pill, color: 'bg-green-500' },
    { name: 'Patienter (demo)', value: '42', icon: Users, color: 'bg-purple-500' },
    { name: 'Akuta tillstånd', value: '30', icon: AlertCircle, color: 'bg-red-500' },
  ]

  const recentDiseases = [
    { name: 'Retinal Avlossning', category: 'Akut', severity: 'Emergency' },
    { name: 'Bakteriell Keratit', category: 'Hornhinna', severity: 'Emergency' },
    { name: 'Akut Glaukom', category: 'Glaukom', severity: 'Emergency' },
  ]

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-3xl font-bold text-gray-900 flex items-center gap-3">
          <Eye className="w-8 h-8 text-primary-600" />
          Eye Care Secretary - Ögonsekreterare
        </h1>
        <p className="mt-2 text-gray-600">
          AI-driven medicinsk kunskapsbas för ögonvård
        </p>
      </div>

      {/* Stats */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat) => {
          const Icon = stat.icon
          return (
            <div key={stat.name} className="card">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm text-gray-600">{stat.name}</p>
                  <p className="text-3xl font-bold mt-2">{stat.value}</p>
                </div>
                <div className={`${stat.color} p-3 rounded-lg`}>
                  <Icon className="w-6 h-6 text-white" />
                </div>
              </div>
            </div>
          )
        })}
      </div>

      {/* Recent Diseases */}
      <div className="card">
        <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
          <AlertCircle className="w-5 h-5 text-red-500" />
          Akuta tillstånd
        </h2>
        <div className="space-y-3">
          {recentDiseases.map((disease, idx) => (
            <div
              key={idx}
              className="flex items-center justify-between p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
            >
              <div>
                <p className="font-medium">{disease.name}</p>
                <p className="text-sm text-gray-600">{disease.category}</p>
              </div>
              <span className="px-3 py-1 bg-red-100 text-red-800 rounded-full text-sm font-medium">
                {disease.severity}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Quick Actions */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="card hover:shadow-md transition-shadow cursor-pointer">
          <Database className="w-8 h-8 text-primary-600 mb-3" />
          <h3 className="font-semibold mb-2">Sök sjukdomar</h3>
          <p className="text-sm text-gray-600">
            Tillgång till 200 ögonsjukdomar med detaljerad information
          </p>
        </div>
        <div className="card hover:shadow-md transition-shadow cursor-pointer">
          <Pill className="w-8 h-8 text-green-600 mb-3" />
          <h3 className="font-semibold mb-2">Läkemedelsdatabas</h3>
          <p className="text-sm text-gray-600">
            100 ögonläkemedel med dosering och biverkningar
          </p>
        </div>
        <div className="card hover:shadow-md transition-shadow cursor-pointer">
          <Eye className="w-8 h-8 text-purple-600 mb-3" />
          <h3 className="font-semibold mb-2">Symtomchecker</h3>
          <p className="text-sm text-gray-600">
            AI-driven symptomanalys och differentialdiagnostik
          </p>
        </div>
      </div>
    </div>
  )
}
