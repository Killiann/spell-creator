async function getForms() {
  const res = await fetch("http://localhost:8000/forms", {
    cache: "no-store",
  });

  if (!res.ok) {
    throw new Error("Failed to fetch forms");
  }

  return res.json();
}

export default async function FormsPage() {
  const forms = await getForms();

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-6">Forms</h1>

      <table className="min-w-full border border-gray-300">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-2 border">Magic School</th>
            <th className="p-2 border">Latin</th>
            <th className="p-2 border">Sanskrit</th>
            <th className="p-2 border">Gaelic</th>
            <th className="p-2 border">Polynesian</th>
            <th className="p-2 border">Bénoué</th>
            <th className="p-2 border">Algonquian</th>            
            <th className="p-2 border">Binary</th>
          </tr>
        </thead>

        <tbody>
          {forms.map((form: any) => (
            <tr key={form.id} className="hover:bg-gray-50">                              
              <td className="p-2 border">{form.spell_school}</td>
              <td className="p-2 border">{form.latin_title}</td>
              <td className="p-2 border">{form.sanskrit_title}</td>
              <td className="p-2 border">{form.gaelic_title}</td>
              <td className="p-2 border">{form.polynesian_title}</td>
              <td className="p-2 border">{form.benoue_title}</td>
              <td className="p-2 border">{form.algonquian_title}</td>
              <td className="p-2 border">{form.binary_code}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
