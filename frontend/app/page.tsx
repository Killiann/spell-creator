import Image from "next/image";
import { getForms, getPowers, getShapes, getTargets, getTechniques } from "@/lib/api";
import { API_Form, API_Power, API_Shape, API_SubTechnique, API_Target, API_Technique, } from "@/types/api_types";
import Tabs from "@/components/tabs";

export default async function Home() {

  const forms: API_Form[] = await getForms();
  const powers: API_Power[] = await getPowers();
  const shapes: API_Shape[] = await getShapes();
  const targets: API_Target[] = await getTargets();
  const techniques: API_Technique[] = await getTechniques();

  return (
    <div className="max-w-6xl mx-auto p-8 w-full h-screen flex flex-col">
      <main className="flex-1 overflow-hidden p-8">
        <img src="title.png"></img>

        <Tabs
          tabs={[
            {
              label: "Forms",
              content: (
                <>
                <table className="min-w-full">
                  <thead>
                    <tr>
                      <th className="p-2 border">Magic School</th>
                      <th className="p-2 border">Latin</th>
                      
                      <th className="p-2 border">Binary</th>
                    </tr>
                  </thead>

                  <tbody>
                    {forms.map((form: API_Form) => (
                      <tr key={form.id} className="hover:bg-gray-50">
                        <td className="p-2 border">{form.spell_school}</td>
                        <td className="p-2 border">{form.latin_title}</td>
                        <td className="p-2 border">{form.binary_code}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>

                <p>Sanskrit: </p>
                    
                </>
                // <th className="p-2 border">Sanskrit</th>
                //       <th className="p-2 border">Gaelic</th>
                //       <th className="p-2 border">Polynesian</th>
                //       <th className="p-2 border">Bénoué</th>
                //       <th className="p-2 border">Algonquian</th>

                        //                 <td className="p-2 border">{form.sanskrit_title}</td>
                        // <td className="p-2 border">{form.gaelic_title}</td>
                        // <td className="p-2 border">{form.polynesian_title}</td>
                        // <td className="p-2 border">{form.benoue_title}</td>
                        // <td className="p-2 border">{form.algonquian_title}</td>
              )
            },
            {
              label: "Powers",
              content: (
                <table className="min-w-full">
                  <thead>
                    <tr>
                      <th className="p-2 border">Tier</th>
                      <th className="p-2 border">Binary Code</th>
                    </tr>
                  </thead>

                  <tbody>
                    {powers.map((power: API_Power) => (
                      <tr key={power.id} className="hover:bg-gray-50">
                        <td className="p-2 border">{power.tier}</td>
                        <td className="p-2 border">{power.binary_code}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )
            },
            {
              label: "Shapes",
              content: (
                <table className="min-w-full">
                  <thead>
                    <tr>
                      <th className="p-2 border">Delivery</th>
                      <th className="p-2 border">Type</th>
                      <th className="p-2 border">Binary Code</th>
                    </tr>
                  </thead>

                  <tbody>
                    {shapes.map((shape: API_Shape) => (
                      <tr key={shape.id} className="hover:bg-gray-50">
                        <td className="p-2 border">{shape.delivery_name}</td>
                        <td className="p-2 border">{shape.delivery_type}</td>
                        <td className="p-2 border">{shape.binary_code}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )
            },
            {
              label: "Targets",
              content: (
                <table className="min-w-full">
                  <thead>
                    <tr>
                      <th className="p-2 border">Name</th>
                      <th className="p-2 border">Binary Code</th>
                      <th className="p-2 border">Connected</th>
                    </tr>
                  </thead>

                  <tbody>
                    {targets.map((target: API_Target) => (
                      <tr key={target.id} className="hover:bg-gray-50">
                        <td className="p-2 border">{target.name}</td>
                        <td className="p-2 border">{target.binary_code}</td>
                        <td className="p-2 border">{target.binary_code_connected}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              )
            },
            {
              label: "Techniques",
              content: (
                <table className="min-w-full">
                  <thead>
                    <tr>
                      <th className="p-2 border">Name</th>
                      <th className="p-2 border">Binary Code</th>
                    </tr>
                  </thead>

                  <tbody>
                    {techniques.map((technique: API_Technique) => (
                      <>
                        <tr key={technique.id} className="hover:bg-gray-50">
                          <td className="p-2 border"><b>{technique.name}</b></td>
                          <td className="p-2 border">{technique.binary_code}</td>
                        </tr>
                        {technique.sub_techniques.map((sub_tech: API_SubTechnique) => (
                          <tr key={sub_tech.id} className="bg-gray-50">
                            <td className="p-2 border">- {sub_tech.name}</td>
                            <td className="p-2 border">{sub_tech.binary_code}</td>
                          </tr>
                        ))}
                      </>
                    ))}
                  </tbody>
                </table>
              )
            }
          ]}>

        </Tabs>
      </main>
    </div>
  );
}
